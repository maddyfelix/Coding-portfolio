import edu.fcps.karel2.Robot;
import edu.fcps.karel2.Display;

public class Athlete1 extends Robot
{

   public Athlete1(int x, int y, int dir, int beep)
   {
      super(x, y, dir, beep);
   }

   public void turnAround()
   {
      turnLeft();
      turnLeft();
   
   }

   public void turnRight() 
   {
      turnLeft();
      turnLeft();
      turnLeft();
   
   }
   public static void main(String[] args) 
   {
   
   }
}