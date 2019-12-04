#include <iostream>
#include <cstring>

void parse_arguments(int &argc, const char* argv[]){
    if (argc < 2){
        std::cout << "not enough pylons\n";
        exit(1);
    }

    if (std::strcmp(argv[1] , "client")== 0){
        std::cout << "client jdfsjf\n";
        //something client related
        return;
    }
    else
    {
	    std::cout << "err\n";
	    std::cout << argv[1];
    }
    //else if (*argv[1] == "server"){
    //    //somthing serverlike
    //    std::cout << "SERVER related stuff booting\n";
    //    return;
    //}
    //else{
    //std::cout << "Input is onzim\n";
    //exit(1);
    //}

}

int main(int argc, char const *argv[])
{
    parse_arguments(argc, argv);
    return 0;
}
