package revolutioner.commands;

import org.kohsuke.args4j.Argument;
import org.kohsuke.args4j.Option;

import java.io.File;
import java.util.List;
import java.util.ArrayList;

public class RecreateCommand implements Command {
    
    @Option(name="--test-data")
    private File optionalTestData;

    @Option(name="--db-version")
    private String optionalDbVersion;

    @Option(name="--no-checks")
    private boolean drop;
    
    @Option(name="--skeleton")
    private boolean skeleton;

    @Argument
    private List <String> arguments = new ArrayList <String>();

	public void run() {
		// TODO Auto-generated method stub
		
	}
}