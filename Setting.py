import os
from configparser import ConfigParser
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# 引用外部配置文件
parser = ConfigParser()
BASE_DIR = Path(__file__).resolve().parent

# 配置文件路径
if os.path.exists(os.path.join(BASE_DIR, 'config_local.conf')):
    conf_path = os.path.join(BASE_DIR, 'config_local.conf')
    print('加载本地环境配置')
else:
    conf_path = os.path.join(BASE_DIR, 'config_pro.conf')
    print('加载线上环境配置')

# 读取配置文件
parser.read(conf_path)

# -----------------------------------------------------------------------------------------------------
# mysql配置
SQLALCHEMY_DATABASE_URL = parser.get('mysql', 'url')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
# 共享的session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 多线程创建多个session用
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SingleSession = scoped_session(SessionFactory)

Base = declarative_base()
# -----------------------------------------------------------------------------------------------------
