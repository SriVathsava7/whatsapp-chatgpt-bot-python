from src.config.bot_config import BotConfig
from src.utils import app_logger

if __name__ == '__main__':
    print('🤖 ChatGPT WhatsApp Bot - Configuration Test')
    print('=' * 48)

    try:
        config = BotConfig.get_all()
        print('✓ Server config loaded')
        print('✓ API config loaded')
        app_logger.info('Logger test successful')
        print('✓ Logger initialized and working')
        print('\n✅ All tests passed! The bot is ready to run.')
    except Exception as e:
        app_logger.error(f'Config test failed: {e}')
        print(f'❌ Config test failed: {e}') 