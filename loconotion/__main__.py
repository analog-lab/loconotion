import os
import sys

import boto3

import modules.main as main


def _exit():
    try:
        sys.exit(1)
    except SystemExit:
        os._exit(1)


if __name__ == "__main__":
    try:
        args = main.get_args()
        log = main.setup_logging(args)
        parser = main.init_parser(args, log)
        parser.run()

        parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        target_dir = parent_directory + f'/dist/{args.page}'

        s3 = boto3.client('s3', aws_access_key_id="AKIASRLALMPPRVY36GVI", aws_secret_access_key=args.key)

        for file in os.listdir(target_dir):
            bucket_name = 'docs.mooda.me'
            file_path = os.path.join(target_dir, file)
            try:
                if file == f'{args.page}.html':
                    s3.upload_file(file_path, bucket_name, file.replace(".html", ""), ExtraArgs={'ContentType': 'text/html'})
                elif file.find(".svg") > 0:
                    s3.upload_file(file_path, bucket_name, file, ExtraArgs={'ContentType': 'image/svg+xml'})
                else:
                    s3.upload_file(file_path, bucket_name, file)
                print(f"업로드 성공: {file}")
            except Exception as e:
                print(f"업로드 실패: {e}")
    except KeyboardInterrupt:
        log.critical("Interrupted by user")
        _exit()
    except Exception as ex:
        if args.verbose:
            log.exception(ex)
        else:
            log.critical(f"{ex.__class__.__name__}: {str(ex)}")
        _exit()
