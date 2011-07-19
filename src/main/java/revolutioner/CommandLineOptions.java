package revolutioner;

import org.kohsuke.args4j.Argument;
import org.kohsuke.args4j.Option;

import java.util.List;
import java.util.ArrayList;

public class CommandLineOptions {
    
    @Option(name="-m", usage="migrate schemas")
    private boolean migrate;

    @Option(name="-r", usage="recreate schemas")
    private boolean recreate;

    @Option(name="-d", usage="drop schemas")
    private boolean drop;

    // receives other command line parameters than options
    @Argument
    private List <String> arguments = new ArrayList <String>();
}