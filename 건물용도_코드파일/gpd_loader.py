import geopandas as gpd
import os

dir_path = '용도별건물공간확보_부산'

def get_gpd(dir_path):
    df_dict = {}
    자치구_list = [name for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name))] #자치구 리스트를 가져오고
    for folder in 자치구_list: #각 자치구 별로
        folder_path = os.path.join(dir_path, folder) #폴더 경로를 만들고 
        shp_files = [file for file in os.listdir(folder_path) if file.endswith('.shp')] #shp 파일이름만 빼오고
    
        for shp_file in shp_files: 
            shp_path = os.path.join(folder_path, shp_file) #자치구별 shp 파일 경로 만들기
            df = gpd.read_file(shp_path, encoding='cp949')
            df_dict[folder] = df
    return 자치구_list, df_dict
