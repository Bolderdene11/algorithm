import java.io.*;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;

public class ReaderTest {
    private Reader reader = new Reader();

    private static final String CLI_FILE = System.getProperty("testFile");

    @Test
    public void testEmptyNull() throws IOException {
        if (CLI_FILE == null) {
            File temp = File.createTempFile("nothing", ".txt");
            String temp_path = temp.getAbsolutePath();
            String result = reader.read(temp_path);
            assertEquals("", result);
            temp.delete();
        } else {
            String expected = new String(java.nio.file.Files.readAllBytes(new File(CLI_FILE).toPath()));
            String result = reader.read(CLI_FILE);
            assertEquals(expected.trim(), result);
        }
    }

    @Test
    public void testFileNonExists() throws IOException {
        if (CLI_FILE == null) {

            String path = "nothing.txt";
            String result = reader.read(path);
            assertNull(result);
        } else {
            String expected = new String(java.nio.file.Files.readAllBytes(new File(CLI_FILE).toPath()));
            String result = reader.read(CLI_FILE);
            assertEquals(expected.trim(), result);
        }
    }
    @Test
    public void testLetter() throws IOException {
        if (CLI_FILE == null){
            File temp = File.createTempFile("letter", "txt");
            FileWriter writer = new FileWriter(temp);
            writer.write("a, b, c");
            writer.close();
            String temp_path = temp.getAbsolutePath();
            String result = reader.read(temp_path);
            int[] numbers = reader.create_array(result);
            assertNull(numbers);
            temp.delete();
        }
        else{
            String result = reader.read(CLI_FILE);
            int[] numbers = reader.create_array(result);
            assertNull(numbers);
        }
    }
    
    public static void main(String[] args) throws IOException{
        Reader reader = new Reader();
        String str_result = reader.read("array1.txt");
        int[] arr = reader.create_array(str_result);

        Sort obj = new Sort();
        
        int[] result = obj.insertion_sort(arr);
        System.out.println("insertion sort: " + Arrays.toString(result));

        int[] arr1 = arr;
        int[] arr2 = arr;

        obj.merge_sort(arr1);
        System.out.println("Merge sort: " + Arrays.toString(arr1));

        BST tree = new BST();
        for (int val : arr2){
            tree.insert(val);
        }
        System.out.println("search 2 in tree: " + tree.search(2));

        System.out.println("Max by divide and conquer: " + obj.get_max(arr, 0, (arr.length - 1)));

    }
}
