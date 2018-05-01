def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    #body = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
    body = [bytes('\r\n'.join(env['QUERY_STRING'].split('&'))).encode("utf-8")]
    return body
