import java.util.ArrayList;
import java.util.List;

public class run_java {

    public static void main(String[] args) {
        Integer start_num = Integer.parseInt(args[0]);
        Integer count = Integer.parseInt(args[1]);

        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < count; ++i) {
            list.add(i * start_num);
        }

        Integer sum = 0;
        Integer divisible = 0;

        for (Integer num : list) {
            sum += num;
            if (num % 10 == 0) ++divisible;
        }

        System.out.println(sum + " " + divisible);
    }

}
