bonus_time = lambda s, b: f"${s*10}" if b else f"${s}"

bonus_time=lambda s,b:f'${s*10*b or s}'
