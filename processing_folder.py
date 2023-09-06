from pathlib import Path
import shutil
import os
import concurrent.futures
# from concurrent.futures import ThreadPoolExecuto



def move_files(path):

   imeges = ['jpeg', 'png', 'jpg', 'svg']
   documents = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']
   audio = ['mp3', 'ogg', 'wav', 'amr']
   video = ['avi', 'mp4', 'mov', 'mkv']
   archives = ['zip', 'gz', 'tar']
   Spisok_papok = ('imeges','documents','audio','video','archives')
   
   # створюєм папки
   for folder in Spisok_papok:
      if not os.path.exists(f'{path}\\{folder}'):
         os.mkdir(f'{path}\\{folder}')


   Spisok = os.listdir(path)  
   for file in Spisok :
         extension = file.split(".")
            #збираю всі розширення
       
       
         if  len(extension) > 1 and extension[-1].lower() in imeges :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'imeges',file)
            shutil.move(old_path,new_path) 
            list_foto = os.listdir(os.path.join(path,'imeges')) 
         elif  len(extension) > 1 and extension[-1].lower() in documents :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'documents',file)
            shutil.move(old_path,new_path)
            list_doc  = os.listdir(os.path.join(path,'documents'))
         elif  len(extension) > 1 and extension[-1].lower() in audio :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'audio',file)
            shutil.move(old_path,new_path) 
            list_music =  os.listdir(os.path.join(path,'audio'))  
         elif  len(extension) > 1 and extension[-1].lower() in video :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'video',file)
            shutil.move(old_path,new_path) 
            list_video = os.listdir(os.path.join(path,'video'))  
         elif  len(extension) > 1 and extension[-1].lower() in archives :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'archives',file)
            shutil.move(old_path,new_path)
            list_archiv =os.listdir(os.path.join(path,'archives'))
         else :
            list_neizvestnie =os.listdir(os.path.join(path))


   print ({  
              'list_music':  list_music,
              'list_video': list_video,
              'list_foto': list_foto,
              'list_doc': list_doc,
              'list_archiv': list_archiv,
            # 'list_vse_razresh': list_vse_razresh,
              'list_neizvestnie': list_neizvestnie,
            })
   
   # list_vse_razresh = set(razresh)   
   # list_neizvestnie = path.glob('*.*')     
                 # Перелік всіх розширень, які скрипту невідомі.

def del_pattern(path):

   Spisok_papok = ('imeges','documents','audio','video','archives')
   pattern_parsinga = path.iterdir()

   for i in pattern_parsinga:

               if  i.is_dir():                
                  if i.name in Spisok_papok:
                     print(f'Не видаляти папку  {i.name} ')
                  else:
                     print(f'Цю папку {i.name} потрібно видалити')   
                     try:
                           os.rmdir(i)
                     except: OSError
                     else:
                           print(f' Папка {i} видалена')
                     finally:
                           print('Зробленно  -----')

   

if __name__ == '__main__': 
      while True:
                path = Path(input('Enter the path of the folder where you want to sort files\n("Введіть путь папки де потрібно зробити сортування файлів"): '))
                if len(str(path)) <= 1:
                    print ("--You didn't lead anything, try another path\n   ('ви нічого не вели, спробуй другой шляx')\n--------------------------------------")
                     
                else :      
                    try:
                        executor =  concurrent.futures.ThreadPoolExecutor(4)
                        executor.submit(move_files,path)
                        del_pattern(path)
                        break
                    except :
                        print ('The path to the folder was not found\n ("Путь к папке не знайден")\n ------------------------------------------------------------------ ')
                        break
      
