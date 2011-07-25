package revolutioner.commands;

import org.kohsuke.args4j.Argument;
import java.io.*;
import java.net.URL;

import revolutioner.Command;

import java.util.List;
import java.util.ArrayList;

public class Help implements Command {

	@Argument
	private List<String> arguments = new ArrayList<String>();

	public void run() {
		URL helpTextFile = getClass().getClassLoader().getResource("help.txt");
		BufferedReader in;
		try {
			in = new BufferedReader(new InputStreamReader(helpTextFile.openStream()));
			String inputLine;
			while ((inputLine = in.readLine()) != null) {
				System.out.println(inputLine);
			}
			in.close();
		} catch (IOException e) {
			System.err.println("I was not able to display the help text - problem loading it from the classpath.");
			e.printStackTrace();
		}
	}
}