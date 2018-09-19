#include <iostream>

void parse_arguments(int &argc, const char* argv[]){
    if (argc < 2){
        std::cout << "not enough pylons\n";
        exit(1);
    }
    // else
    //     std::cout<<argv[1]<<std::endl;


    
    if (*argv[1] == "client"){
        //something client related
        return;
    }
    else if (*argv[1] == "server"){
        //somthing serverlike
        std::cout << "SERVER related stuff booting\n";
        return;
    }
    else{
    std::cout << "Input is onzim\n";
    exit(1);
    }
    
}

int main(int argc, char const *argv[])
{
    parse_arguments(argc, argv);
    return 0;
}
