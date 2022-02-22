from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000" # 포트 지정 안 하면 CORS 에러 발생
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from functions import (
    create_upload_file, 

    get_head, 
    get_tail, 
    get_shape,
    get_dtype,
    get_columns,
    get_unique,
    # get_unique_column,
    get_na,
    get_corr,
    get_describe,
    get_col_condition,
    get_loc,
    get_iloc,

    set_transpose,
    set_groupby,
    set_drop,
    set_dropna,
    set_rename,
    set_sort_values,
    set_merge,
    set_concat,
    set_column
)

create_upload_file = app.post("/uploadfile")               (create_upload_file)
get_head           = app.post("/dataframe/head")           (get_head)
get_tail           = app.post("/dataframe/tail")           (get_tail)
get_shape          = app.post("/dataframe/shape")          (get_shape)
get_dtype          = app.post("/dataframe/dtype")          (get_dtype)
get_columns        = app.post("/dataframe/columns")        (get_columns)
get_unique         = app.post("/dataframe/unique")         (get_unique)
# get_unique_column  = app.post("/dataframe/unique/{column}")(get_unique_column)
get_na             = app.post("/dataframe/isna")           (get_na)
get_corr           = app.post("/dataframe/corr")           (get_corr)
get_describe       = app.post("/dataframe/describe")       (get_describe)
get_col_condition  = app.post("/dataframe/col_condition")  (get_col_condition)
get_loc            = app.post("/dataframe/loc")            (get_loc)
get_iloc           = app.post("/dataframe/iloc")           (get_iloc)





from functions import (box_plot)

box_plot = app.get("/plot/boxplot")(box_plot)


set_transpose      = app.post("/dataframe/transpose")      (set_transpose)
set_groupby        = app.post("/dataframe/groupby")        (set_groupby)
set_drop           = app.post("/dataframe/drop")           (set_drop)
set_dropna         = app.post("/dataframe/dropna")         (set_dropna)
set_rename         = app.post("/dataframe/rename")         (set_rename)
set_sort_values    = app.post("/dataframe/sort_values")    (set_sort_values)
# set_sort_index     = app.post("/dataframe/sort/index")     (set_sort_index)
set_merge          = app.post("/dataframe/merge")          (set_merge)
set_concat         = app.post("/dataframe/concat")         (set_concat)
set_column         = app.post("/dataframe/set_column")     (set_column)