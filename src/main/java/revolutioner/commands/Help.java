package revolutioner.commands;

import org.kohsuke.args4j.Argument;

import revolutioner.Command;

import java.util.List;
import java.util.ArrayList;

public class Help implements Command {
	
    @Argument
    private List <String> arguments = new ArrayList <String>();

	public void run() {
		// TODO Auto-generated method stub
		
	}
}