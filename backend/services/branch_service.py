from sqlalchemy.orm import Session

from models.branch import Branch


def create_branch_service(
    db: Session,
    branch
):

    new_branch = Branch(
        name=branch.name,
        location=branch.location
    )

    db.add(new_branch)

    db.commit()

    db.refresh(new_branch)

    return new_branch


def get_branches_service(db: Session):

    return db.query(Branch).all()