from fastapi import FastAPI

from repos.sqlite_repo import SQLiteRepo
from use_cases.product_list import product_list_use_case

app = FastAPI()


@app.get('/products')
def get_products():
    repo = SQLiteRepo(connection_info={})
    result = product_list_use_case(repo, params={})
    return result


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
