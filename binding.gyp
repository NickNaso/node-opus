# Test

{
    'variables': {
    },
    'targets': [
        {
            'target_name': 'node-opus',
            'dependencies': [
                'deps/binding.gyp:libopus'
            ],
            'cflags!': [ '-fno-exceptions' ],
            'cflags_cc!': [ '-fno-exceptions' ],
            'cflags': [
                '-pthread',
                '-fno-exceptions',
                '-fno-strict-aliasing',
                '-Wall',
                '-Wno-unused-parameter',
                '-Wno-missing-field-initializers',
                '-Wextra',
                '-pipe',
                '-fno-ident',
                '-fdata-sections',
                '-ffunction-sections',
                '-fPIC'
            ],
            'defines': [
                'LARGEFILE_SOURCE',
                '_FILE_OFFSET_BITS=64',
                'WEBRTC_TARGET_PC',
                'WEBRTC_LINUX',
                'WEBRTC_THREAD_RR',
                'EXPAT_RELATIVE_PATH',
                'GTEST_RELATIVE_PATH',
                'JSONCPP_RELATIVE_PATH',
                'WEBRTC_RELATIVE_PATH',
                'POSIX',
                '__STDC_FORMAT_MACROS',
                'DYNAMIC_ANNOTATIONS_ENABLED=0'
            ],
            'include_dirs': [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            'dependencies': [
                "<!(node -p \"require('node-addon-api').gyp\")"
            ],
            'sources': [
                'src/node-opus.cc',
            ],
            'xcode_settings': {
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                'CLANG_CXX_LIBRARY': 'libc++',
                'MACOSX_DEPLOYMENT_TARGET': '10.7',
            },
            'msvs_settings': {
                'VCCLCompilerTool': { 'ExceptionHandling': 1 },
            },
            'link_settings': {
                'ldflags': [
                ],
                'libraries': [
                ]
            }
        }
    ]
}
