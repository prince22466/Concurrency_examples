import Yaml_pipline_excutor

if __name__ == "__main__":

    ymal_pipline_excut = Yaml_pipline_excutor.Yaml_pipline_Excute(
                                ymal_file='piplines\wiki_YF_scrapper_pipline.yaml'
                                )
    
    ymal_pipline_excut.process_pipline()

    print("All finished")
    exit()