import dlt


INPUT_TABLE_NAME = "florent_moiny.test_dlt_read.input_table"
DLT_TABLE_NAME = "table_02"


@dlt.table(name=DLT_TABLE_NAME)
def streaming_table():
  return spark.readStream.format("delta").table(INPUT_TABLE_NAME)
