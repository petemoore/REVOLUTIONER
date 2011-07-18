package revolutioner;

import org.kohsuke.args4j.CmdLineParser;
import org.kohsuke.args4j.CmdLineException;

/**
 * This is the main app
 */
public class Revolutioner {

    public static void main( String[] args ) {

        try {
            CommandLineOptions bean = new CommandLineOptions();
            CmdLineParser parser = new CmdLineParser(bean);
            parser.parseArgument(args);
        } catch (CmdLineException e) {
            System.out.println("Whoops!");
        }
    }
}
