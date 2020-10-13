import os
import tempfile
import shutil
import zipfile
import glob
import base64
import zipfile

data_dir = "/app/data"
base_dir = os.getcwd()

def get_dirs(path):
    print(os.path.dirname(os.path.join(data_dir, path, '*')))
    return [os.path.basename(x) for x in filter(
        os.path.isdir, glob.glob(os.path.join(data_dir, path, '*')))]


def get_apis():
    return get_dirs('api')


def get_clients():
    return get_dirs('client')


def get_servers():
    return get_dirs('server')


def get_platforms():
    return get_dirs('platform')


def get_databases():
    return ['SQL Server 2017']


def get_project(api='ASP.NET Core 3.1 EF Core 3.8.1', client='Angular 10', server='Nginx', platform="Docker"):
    path = os.path.dirname(os.path.realpath(__file__))

    output_dir = "."
    tmp_dir = tempfile.mkdtemp()

    shutil.copytree(f'{data_dir}/api/{api}', f"{tmp_dir}/api/")
    shutil.copytree(f'{data_dir}/client/{client}', f"{tmp_dir}/client/")
    shutil.copytree(f'{data_dir}/server/{server}', f"{tmp_dir}/server/")
    shutil.copytree(f'{data_dir}/platform/{platform}', f"{tmp_dir}/", dirs_exist_ok=True)

    shutil.make_archive('/tmp/project', 'zip', tmp_dir, tmp_dir)

    with open("/tmp/project.zip", 'rb') as f:
        message_bytes = f.read()
        print(len(message_bytes))
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return base64_message
