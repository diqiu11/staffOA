from config.settings import DevelopmentConfig, ProductionConfig, TestingConfig

# 应用环境变量
config = {
    # 开发环境
    'development': DevelopmentConfig,
    # 测试环境
    'testing': TestingConfig,
    # 生产环境
    'production': ProductionConfig
}
