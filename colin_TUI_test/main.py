import sys
import os

should_restart = True
def set_restart_flag(restart):
    global should_restart
    should_restart = restart

def main():
    global should_restart

    while True:
        try:
            from ssh_manager.tui import SSHManagerTUI
            should_restart = True

            app = SSHManagerTUI()
            app.set_restart_callback(set_restart_flag)
            app.run()

            if not should_restart:
                break

          # Exit the loop if the app runs successfully
        except KeyboardInterrupt:
            print("\nFoodbye!")
            break

        except Exception as e:
            print(f"\nError: {e}")
            restart = input("Restart SSH Manager? (y/n): ")
            if restart.lower() not in ['y', 'yes']:
                break

if __name__ == "__main__":
    main()
    