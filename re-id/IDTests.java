import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class IDTests {

    @Test
    public void testProvided0(){
        assertEquals("23571", Solution.solution(0));
    }

    @Test
    public void testProvided3(){
        assertEquals("71113", Solution.solution(3));
    }

    @Test
    public void test10000(){
        assertEquals("02192", Solution.solution(10000));
    }
}