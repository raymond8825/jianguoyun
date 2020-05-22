import java.io.File;
public class Test{
    public static void main(String[] args){
        String path="/Users/liruiping/Desktop/自我介绍.docx";
        File file=new File(path);
        for(String filename:file.list()){
            System.out.println(filename);
        }
    
    }
}