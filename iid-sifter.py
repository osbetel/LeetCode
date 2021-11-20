import os
import pyarrow
import pandas as pd


def test():
    path = os.path.abspath("/Volumes/Main Backup/iid/")
    filedir = os.listdir(path)
    filedir = [x for x in filedir if x.__contains__("date")]
    # print(filedir)

    iids_x = ["7.575481bdf9c249cb95e4c29f895b2b44", "7.534cf1abbad34ba3bbddc5c54bf63754",
            "7.29e9952de4e6455f878dc5179f4a41cf", "7.f4949869163b4f9c838a19f457882628"]

    iids_y = ["7.575481bdf9c249cb95e4c29f895b2b44", "7.534cf1abbad34ba3bbddc5c54bf63754",
              "7.29e9952de4e6455f878dc5179f4a41cf", "7.f4949869163b4f9c838a19f457882628"]

    from time import time
    start = time()
    res = []
    processed_count = 0
    for date in filedir:
        date_path = f"{path}/{date}"
        print(date)
        parquet_files = [x for x in os.listdir(date_path) if x.__contains__("parquet")]

        for file in parquet_files:
            abs_file_path = f"{date_path}/{file}"
            processed_count += 1
            if processed_count % 100 == 0:
                print(f"processed {processed_count} files", time() - start, "s")
            # print(abs_file_path)

            df = pd.read_parquet(abs_file_path, engine="pyarrow")
            df = df[df["iid"].isin(iids_x)]

            if not df.empty:
                print(f"record found for {date}", df)
                res.append((abs_file_path, df))
        print("processed in", time() - start, "s")

k = """[('/Volumes/Main Backup/iid/date=2021-02-07/part-00285-ea0fc521-d299-43d1-a5cc-697925a23dfc-c000.snappy.parquet',                                        iid  count_of
227417  7.29e9952de4e6455f878dc5179f4a41cf         5), ('/Volumes/Main Backup/iid/date=2021-02-08/part-00265-5737ff8c-6f00-407b-81ed-b8b126d7707b-c000.snappy.parquet',                                       iid  count_of
77521  7.575481bdf9c249cb95e4c29f895b2b44         7), ('/Volumes/Main Backup/iid/date=2021-02-09/part-00265-6784deb8-62d3-4578-b624-46372e0e3212-c000.snappy.parquet',                                       iid  count_of
66952  7.575481bdf9c249cb95e4c29f895b2b44        19), ('/Volumes/Main Backup/iid/date=2021-02-10/part-00265-60ffeba9-0fcd-411d-a14f-47a27520e3be-c000.snappy.parquet',                                        iid  count_of
198895  7.575481bdf9c249cb95e4c29f895b2b44         5), ('/Volumes/Main Backup/iid/date=2021-02-10/part-00307-60ffeba9-0fcd-411d-a14f-47a27520e3be-c000.snappy.parquet',                                       iid  count_of
64490  7.f4949869163b4f9c838a19f457882628         7), ('/Volumes/Main Backup/iid/date=2021-02-11/part-00285-4f399b20-62bb-4820-8243-e400e029f352-c000.snappy.parquet',                                        iid  count_of
256536  7.29e9952de4e6455f878dc5179f4a41cf         8), ('/Volumes/Main Backup/iid/date=2021-02-12/part-00285-c1a765b1-5221-43c6-8ba7-a9e3d80df33f-c000.snappy.parquet',                                       iid  count_of
84966  7.29e9952de4e6455f878dc5179f4a41cf        30), ('/Volumes/Main Backup/iid/date=2021-02-13/part-00307-46aace45-c521-4a18-8e04-57937c9ee32e-c000.snappy.parquet',                                       iid  count_of
98604  7.f4949869163b4f9c838a19f457882628        19), ('/Volumes/Main Backup/iid/date=2021-02-14/part-00285-4c3d64f9-3ea3-4cc1-8908-832aba1c6ffb-c000.snappy.parquet',                                       iid  count_of
78687  7.29e9952de4e6455f878dc5179f4a41cf        13), ('/Volumes/Main Backup/iid/date=2021-02-16/part-00285-cdf0e194-1e12-4b2e-892d-74216b5bea0d-c000.snappy.parquet',                                        iid  count_of
288279  7.29e9952de4e6455f878dc5179f4a41cf        14), ('/Volumes/Main Backup/iid/date=2021-02-17/part-00285-2327798e-74b6-4cc7-a1ba-4521f068801f-c000.snappy.parquet',                                        iid  count_of
124532  7.29e9952de4e6455f878dc5179f4a41cf        62), ('/Volumes/Main Backup/iid/date=2021-02-17/part-00307-2327798e-74b6-4cc7-a1ba-4521f068801f-c000.snappy.parquet',                                        iid  count_of
122691  7.f4949869163b4f9c838a19f457882628        41), ('/Volumes/Main Backup/iid/date=2021-02-18/part-00285-c256d4d1-7fbb-4377-8077-3ce411dade2a-c000.snappy.parquet',                                        iid  count_of
277122  7.29e9952de4e6455f878dc5179f4a41cf        23), ('/Volumes/Main Backup/iid/date=2021-02-19/part-00265-a27c2e86-db1c-455f-b7e7-1b11a2a1a8b1-c000.snappy.parquet',                                        iid  count_of
917965  7.575481bdf9c249cb95e4c29f895b2b44         1), ('/Volumes/Main Backup/iid/date=2021-02-21/part-00285-d5c7ef61-c137-4cfa-9c60-88e452164a56-c000.snappy.parquet',                                        iid  count_of
162960  7.29e9952de4e6455f878dc5179f4a41cf        24), ('/Volumes/Main Backup/iid/date=2021-02-22/part-00265-73ad7293-97cb-42cb-8a6c-9eed5d3b4c3e-c000.snappy.parquet',                                        iid  count_of
747633  7.575481bdf9c249cb95e4c29f895b2b44         3), ('/Volumes/Main Backup/iid/date=2021-02-22/part-00285-73ad7293-97cb-42cb-8a6c-9eed5d3b4c3e-c000.snappy.parquet',                                        iid  count_of
429996  7.29e9952de4e6455f878dc5179f4a41cf         6), ('/Volumes/Main Backup/iid/date=2021-02-23/part-00265-46a5fccb-e046-4410-8b45-df4417c30779-c000.snappy.parquet',                                       iid  count_of
76397  7.575481bdf9c249cb95e4c29f895b2b44        35), ('/Volumes/Main Backup/iid/date=2021-02-23/part-00307-46a5fccb-e046-4410-8b45-df4417c30779-c000.snappy.parquet',                                        iid  count_of
111582  7.f4949869163b4f9c838a19f457882628        34), ('/Volumes/Main Backup/iid/date=2021-02-24/part-00265-d2155360-2f73-42b2-ac8b-f2eb5110d10f-c000.snappy.parquet',                                        iid  count_of
535441  7.575481bdf9c249cb95e4c29f895b2b44        11), ('/Volumes/Main Backup/iid/date=2021-02-24/part-00307-d2155360-2f73-42b2-ac8b-f2eb5110d10f-c000.snappy.parquet',                                       iid  count_of
73980  7.f4949869163b4f9c838a19f457882628        74), ('/Volumes/Main Backup/iid/date=2021-02-25/part-00265-9deb6a33-dfa3-4c65-8f45-6bb624261f77-c000.snappy.parquet',                                        iid  count_of
523497  7.575481bdf9c249cb95e4c29f895b2b44         3), ('/Volumes/Main Backup/iid/date=2021-02-26/part-00285-9793593a-ec88-4b27-a304-2a03287ae55d-c000.snappy.parquet',                                        iid  count_of
197448  7.29e9952de4e6455f878dc5179f4a41cf        74), ('/Volumes/Main Backup/iid/date=2021-02-27/part-00285-fa5f0352-f8d2-49d4-badd-b51b6b6aa086-c000.snappy.parquet',                                        iid  count_of
138703  7.29e9952de4e6455f878dc5179f4a41cf        41), ('/Volumes/Main Backup/iid/date=2021-02-28/part-00307-76212201-c35e-4e76-bc7c-13af8b21d50d-c000.snappy.parquet',                                        iid  count_of
117803  7.f4949869163b4f9c838a19f457882628        24)]"""
k = eval(k)
