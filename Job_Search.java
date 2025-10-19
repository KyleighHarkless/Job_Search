import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Job_Search{
    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("fake_jobs.csv"));
            for (String line : lines) {
                System.out.println(line);
            }
        } 
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    static ArrayList<String> searchJobs(String keyword, String location) {
        return new ArrayList<String>();
    }

}