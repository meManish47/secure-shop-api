class EmailSender:
    def send(self, to_id, subject, body):
        # nested helper function
        def format_message(s, b):
            return f"Subject: {s}\n\n{b}"
            
        msg = format_message(subject, body)
        print(f"Sending email to {to_id}...\n{msg}")