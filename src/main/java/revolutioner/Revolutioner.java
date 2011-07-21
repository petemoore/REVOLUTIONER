package revolutioner;

import java.util.Arrays;
import java.util.HashMap;

import org.kohsuke.args4j.CmdLineParser;
import org.kohsuke.args4j.CmdLineException;

import revolutioner.commands.*;

/**
 * This is the main app
 */
public class Revolutioner {
	
	/*
	 * The first parameter that is passed on the command line determines which command to run.
	 * This HashMap maps the command line option to the Command that runs the logic.
	 */
	private static HashMap<String, Command> commandBeanMap = new HashMap<String, Command> ();
	static {
		commandBeanMap.put("migrate", new MigrateCommand());
		commandBeanMap.put("drop", new DropCommand());
		commandBeanMap.put("recreate", new RecreateCommand());
	}

    public static void main( String[] args ) {
    	if (args.length > 1) {
	    	String[] remainingArgs = Arrays.copyOfRange(args, 1, args.length);
	    	String command = args[0];
	    	Command bean = commandBeanMap.get(command);
	        try {
	            CmdLineParser parser = new CmdLineParser(bean);
	            parser.parseArgument(remainingArgs);
	        	bean.run();
	        } catch (CmdLineException e) {
	            System.out.println("Whoops!");
	            e.printStackTrace();
	        }
    	} else {
    		System.out.println("Command usage explanation ...");
    	}
    }
}