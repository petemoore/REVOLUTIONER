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
	 * The first parameter that is passed on the command line determines which
	 * command to run. This HashMap maps the command line option to the Command
	 * that runs the logic.
	 */
	private static HashMap<String, Command> commandBeanMap = new HashMap<String, Command>();
	static {
		commandBeanMap.put("migrate", new Migrate());
		commandBeanMap.put("drop", new Drop());
		commandBeanMap.put("recreate", new Recreate());
	}

	public static void main(String[] args) {
		String firstArg;
		if (args.length >= 1 && (firstArg = args[0]) != null) {
			String[] remainingArgs = Arrays.copyOfRange(args, 1, args.length);
			Command bean = commandBeanMap.get(firstArg);
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