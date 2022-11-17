from fastapi import Query


create_user_validation = Query(default=None, max_length=2)
