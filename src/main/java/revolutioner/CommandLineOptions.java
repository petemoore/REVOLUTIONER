package revolutioner;

import org.kohsuke.args4j.Argument;
import org.kohsuke.args4j.Option;

import java.util.List;
import java.util.ArrayList;

public class CommandLineOptions {
    
    @Option(name="--migrate")
    private boolean migrate;

    @Option(name="--recreate")
    private boolean recreate;

    @Option(name="--drop")
    private boolean drop;

    // receives other command line parameters than options
    @Argument
    private List <String> arguments = new ArrayList <String>();
}