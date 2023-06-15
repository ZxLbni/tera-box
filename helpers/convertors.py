import math
async def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

async def convert_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"

async def progress_text(current, total):
    progress = current / total
    progress_bar_length = 10
    completed_length = int(progress * progress_bar_length)
    remaining_length = progress_bar_length - completed_length

    progress_bar_text = "[ " + "● " * completed_length + "○ " * remaining_length + "]"
    return progress_bar_text