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
		commandBeanMap.put("check", new Check());
		commandBeanMap.put("config", new Config());
		commandBeanMap.put("describe-user", new DescribeUser());
		commandBeanMap.put("drop", new Drop());
		commandBeanMap.put("export", new Export());
		commandBeanMap.put("generate-ctfs", new GenerateCTFs());
		commandBeanMap.put("get-actual", new GetActual());
		commandBeanMap.put("get-expected", new GetExpected());
		commandBeanMap.put("help", new Help());
		commandBeanMap.put("initialise", new Initialise());
		commandBeanMap.put("migrate", new Migrate());
		commandBeanMap.put("recreate", new Recreate());
		commandBeanMap.put("release-report", new ReleaseReport());
		commandBeanMap.put("show-migrations-dir", new ShowMigrationsDir());
	}

	public static void main(String[] args) {
		String command;
		String[] commandArguments;
		if ((args.length == 0) || (args[0] == null)) {
			command = "help";
			commandArguments = new String[] {};
		} else {
			command = args[0];
			commandArguments = Arrays.copyOfRange(args, 1, args.length);
		}

		Command bean = commandBeanMap.get(command);
		if (bean == null) {
			bean = commandBeanMap.get("help");
		}
		
		try {
			CmdLineParser parser = new CmdLineParser(bean);
			parser.parseArgument(commandArguments);
			bean.run();
		} catch (CmdLineException e) {
			e.printStackTrace();
		}
	}
}