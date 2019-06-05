class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        res = []
        if not logs:
            return res
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log.split(' ')[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append([log.split(' ')[0], log.split(' ')[1:]])
        letter_logs = sorted(letter_logs, key = lambda x: x[0])        
        letter_logs = sorted(letter_logs, key = lambda x: x[1])
        for log in letter_logs:
            log_str = log[0]
            for val in log[1]:
                log_str += ' ' + val
            res.append(log_str)
        res = res + digit_logs
        return res