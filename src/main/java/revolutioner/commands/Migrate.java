package revolutioner.commands;

import org.kohsuke.args4j.Argument;
import org.kohsuke.args4j.Option;

import revolutioner.Command;

import java.io.File;
import java.util.List;
import java.util.ArrayList;

public class Migrate implements Command {
    
    @Option(name="--test-data")
    private File optionalTestData;

    @Option(name="--db-version")
    private String optionalDbVersion;

    @Option(name="--no-checks")
    private boolean noChecks;
    
    @Option(name="--skeleton")
    private boolean skeleton;

    @Argument
    private List <String> arguments = new ArrayList <String>();

	public void run() {
		System.out.println("Running a migration!");
		System.out.println("Optional Test data file: " + optionalTestData.getPath());
		System.out.println("Optional Database version: " + optionalDbVersion);
		System.out.println("No checks: " + noChecks);
		System.out.println("Skeleton: " + skeleton);
		System.out.println("Other arguments: " + arguments);
	}
}