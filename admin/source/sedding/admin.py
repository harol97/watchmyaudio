from source.api.admin.user.depends import get_repository, get_service
from source.api.admin.user.dtos import UserIn
from source.dependencies.session import get_session


async def create_user():
    session = next(get_session())
    service = get_service(get_repository(session))
    try:
        await service.get_by_email("administrator@gmail.com")
    except:
        new_user = UserIn(
            name="administrator",
            email="administrator@gmail.com",
            password="administrator",
        )
        await service.create(new_user)
