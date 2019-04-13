using System;
using System.Linq;

class MainClass {
    static void Main(string[] args) {
        int startNum;
        int count;

        Int32.TryParse(args[0], out startNum);
        Int32.TryParse(args[1], out count);

        int sum = 0;
        int div = 0;

        int[] nums = new int[count];
        for (int i = 0; i < count; i++)
            nums[i] = i * startNum;

        sum = nums.Sum();
        div = nums.Count(x => x % 10 == 0);

        System.Console.Write(sum + " " + div);
    }
}
