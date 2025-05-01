import curses

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    
    # Save current terminal state
    curses.def_prog_mode()
    
    # Your curses application here
    stdscr.addstr(0, 0, "Write 'Benja' to quit")
    stdscr.refresh()
    
    input_buffer = ""  # To store user input
    
    while True:
        key = stdscr.getch()
        
        # Handle character input
        if 0 <= key <= 255:
            input_buffer += chr(key)
            stdscr.addstr(1, 0, f"You typed: {input_buffer}")
            
            # Check if last characters match "Benja"
            if len(input_buffer) >= 5 and input_buffer[-5:].lower() == "benja":
                break
        elif key == curses.KEY_BACKSPACE or key == 127:
            # Handle backspace
            input_buffer = input_buffer[:-1]
            stdscr.addstr(1, 0, " " * 20)  # Clear line
            stdscr.addstr(1, 0, f"You typed: {input_buffer}")
        
        stdscr.refresh()
        
        # Example: Temporarily exit curses mode
        if key == ord('\n'):  # Enter key
            curses.reset_shell_mode()  # Return to shell mode
            print("\nTemporarily in normal terminal mode!")
            input("Press Enter to continue...")
            curses.reset_prog_mode()  # Restore program mode
            stdscr.clear()
            stdscr.addstr(0, 0, "Write 'Benja' to quit")
            stdscr.addstr(1, 0, f"You typed: {input_buffer}")
            stdscr.refresh()
        
curses.wrapper(main)