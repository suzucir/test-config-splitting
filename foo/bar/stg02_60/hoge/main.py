import os


if __name__ == "__main__":
    # test env vars injected
    print(os.environ.get("env_no_num", ""))
