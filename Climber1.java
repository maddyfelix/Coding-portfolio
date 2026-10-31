import edu.fcps.karel2.Robot;
import edu.fcps.karel2.Display;


public class Climber1 extends Athlete1
{

Display.openWorld("maps/mountain.map");
Display.setSize(10,10);
Display.setSpeed(10);

   public Climber()
   {
      super();
   }
   public Climber(int x)
   {
      super(x,1,Display.NORTH,1);
   }

   public void climbUpRight(Athlete arg)
   {
      arg.turnLeft();
      arg.move();
      arg.move();
      arg.turnRight();
      arg.move();
   }
   
}
