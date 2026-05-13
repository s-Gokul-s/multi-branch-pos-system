from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.branch_schema import (
    BranchCreate,
    BranchResponse
)

from services.branch_service import (
    create_branch_service,
    get_branches_service
)

from auth.auth_bearer import get_current_user
from auth.role_checker import admin_required


router = APIRouter(
    prefix="/branches",
    tags=["Branches"]
)


@router.post(
    "/",
    response_model=BranchResponse
)
def create_branch(

    branch: BranchCreate,

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    admin_required(current_user)

    return create_branch_service(
        db,
        branch
    )


@router.get(
    "/",
    response_model=list[BranchResponse]
)
def get_branches(

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    return get_branches_service(db)