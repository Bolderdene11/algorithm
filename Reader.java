import java.io.*;
import java.util.Arrays;

public class Reader {

    public String read(String path) throws IOException{
        File file = new File(path);
        StringBuilder text = new StringBuilder();
        try {
            FileReader reader = new FileReader(file);
            BufferedReader breader = new BufferedReader(reader);
            String line;
            while ((line = breader.readLine()) != null){        
                text.append(line).append("\n");                
            }
            breader.close();
        }
            
        catch (FileNotFoundException e){
            System.out.println("File not found: " + e.getMessage());
            return null;
        } 
        catch (IOException e){
            System.out.println("IO error: " + e.getMessage());
        }
        catch (Exception e){
            System.out.println("Unexpected error: " + e.getMessage());
            return null;
        }
        finally {
            System.out.println("Done");
        }
        return text.toString().trim();
    }

    public int[] create_array(String text) throws IOException{
        try{
            text = text.replace(", ", " ").replace("\n", " ").replace("\r", " ").replace("\t", " ");
            String[] items = text.split("\\s+");
            int[] result = new int[items.length];

            for (int i = 0;i<items.length;i++){
                result[i] = Integer.parseInt(items[i]);
            }
            return result;
        }
        catch (NumberFormatException e){
            System.out.println(("Invalid number format: " + e.getMessage()));     
            return null;
        }
        finally{
            System.out.println("Done");
        }
        
    }

    public static void main(String[] args) throws IOException{
        Reader reader = new Reader();
        String result = reader.read("test.txt");
        int[] result1 = reader.create_array(result);
        System.out.println(Arrays.toString(result1));
    }
}
