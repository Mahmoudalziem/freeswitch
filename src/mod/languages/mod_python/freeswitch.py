# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_freeswitch', [dirname(__file__)])
        except ImportError:
            import _freeswitch
            return _freeswitch
        if fp is not None:
            try:
                _mod = imp.load_module('_freeswitch', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _freeswitch = swig_import_helper()
    del swig_import_helper
else:
    import _freeswitch
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def setGlobalVariable(*args):
  return _freeswitch.setGlobalVariable(*args)
setGlobalVariable = _freeswitch.setGlobalVariable

def getGlobalVariable(*args):
  return _freeswitch.getGlobalVariable(*args)
getGlobalVariable = _freeswitch.getGlobalVariable

def consoleLog(*args):
  return _freeswitch.consoleLog(*args)
consoleLog = _freeswitch.consoleLog

def consoleLog2(*args):
  return _freeswitch.consoleLog2(*args)
consoleLog2 = _freeswitch.consoleLog2

def consoleCleanLog(*args):
  return _freeswitch.consoleCleanLog(*args)
consoleCleanLog = _freeswitch.consoleCleanLog

def running():
  return _freeswitch.running()
running = _freeswitch.running

def email(*args):
  return _freeswitch.email(*args)
email = _freeswitch.email
class IVRMenu(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IVRMenu, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IVRMenu, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _freeswitch.new_IVRMenu(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _freeswitch.delete_IVRMenu
    __del__ = lambda self : None;
    def bindAction(self, *args): return _freeswitch.IVRMenu_bindAction(self, *args)
    def execute(self, *args): return _freeswitch.IVRMenu_execute(self, *args)
IVRMenu_swigregister = _freeswitch.IVRMenu_swigregister
IVRMenu_swigregister(IVRMenu)

class API(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, API, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, API, name)
    __repr__ = _swig_repr
    def __init__(self, s=None): 
        this = _freeswitch.new_API(s)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _freeswitch.delete_API
    __del__ = lambda self : None;
    def execute(self, *args): return _freeswitch.API_execute(self, *args)
    def executeString(self, *args): return _freeswitch.API_executeString(self, *args)
    def getTime(self): return _freeswitch.API_getTime(self)
API_swigregister = _freeswitch.API_swigregister
API_swigregister(API)

class input_callback_state_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, input_callback_state_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, input_callback_state_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["function"] = _freeswitch.input_callback_state_t_function_set
    __swig_getmethods__["function"] = _freeswitch.input_callback_state_t_function_get
    if _newclass:function = _swig_property(_freeswitch.input_callback_state_t_function_get, _freeswitch.input_callback_state_t_function_set)
    __swig_setmethods__["threadState"] = _freeswitch.input_callback_state_t_threadState_set
    __swig_getmethods__["threadState"] = _freeswitch.input_callback_state_t_threadState_get
    if _newclass:threadState = _swig_property(_freeswitch.input_callback_state_t_threadState_get, _freeswitch.input_callback_state_t_threadState_set)
    __swig_setmethods__["extra"] = _freeswitch.input_callback_state_t_extra_set
    __swig_getmethods__["extra"] = _freeswitch.input_callback_state_t_extra_get
    if _newclass:extra = _swig_property(_freeswitch.input_callback_state_t_extra_get, _freeswitch.input_callback_state_t_extra_set)
    __swig_setmethods__["funcargs"] = _freeswitch.input_callback_state_t_funcargs_set
    __swig_getmethods__["funcargs"] = _freeswitch.input_callback_state_t_funcargs_get
    if _newclass:funcargs = _swig_property(_freeswitch.input_callback_state_t_funcargs_get, _freeswitch.input_callback_state_t_funcargs_set)
    def __init__(self): 
        this = _freeswitch.new_input_callback_state_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _freeswitch.delete_input_callback_state_t
    __del__ = lambda self : None;
input_callback_state_t_swigregister = _freeswitch.input_callback_state_t_swigregister
input_callback_state_t_swigregister(input_callback_state_t)

S_HUP = _freeswitch.S_HUP
S_FREE = _freeswitch.S_FREE
S_RDLOCK = _freeswitch.S_RDLOCK
class DTMF(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DTMF, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DTMF, name)
    __repr__ = _swig_repr
    __swig_setmethods__["digit"] = _freeswitch.DTMF_digit_set
    __swig_getmethods__["digit"] = _freeswitch.DTMF_digit_get
    if _newclass:digit = _swig_property(_freeswitch.DTMF_digit_get, _freeswitch.DTMF_digit_set)
    __swig_setmethods__["duration"] = _freeswitch.DTMF_duration_set
    __swig_getmethods__["duration"] = _freeswitch.DTMF_duration_get
    if _newclass:duration = _swig_property(_freeswitch.DTMF_duration_get, _freeswitch.DTMF_duration_set)
    def __init__(self, *args): 
        this = _freeswitch.new_DTMF(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _freeswitch.delete_DTMF
    __del__ = lambda self : None;
DTMF_swigregister = _freeswitch.DTMF_swigregister
DTMF_swigregister(DTMF)

class Stream(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Stream, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Stream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _freeswitch.new_Stream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _freeswitch.delete_Stream
    __del__ = lambda self : None;
    def read(self, *args): return _freeswitch.Stream_read(self, *args)
    def write(self, *args): return _freeswitch.Stream_write(self, *args)
    def raw_write(self, *args): return _freeswitch.Stream_raw_write(self, *args)
    def get_data(self): return _freeswitch.Stream_get_data(self)
Stream_swigregister = _freeswitch.Stream_swigregister
Stream_swigregister(Stream)

class Event(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Event, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Event, name)
    __repr__ = _swig_repr
    __swig_setmethods__["event"] = _freeswitch.Event_event_set
    __swig_getmethods__["event"] = _freeswitch.Event_event_get
    if _newclass:event = _swig_property(_freeswitch.Event_event_get, _freeswitch.Event_event_set)
    __swig_setmethods__["serialized_string"] = _freeswitch.Event_serialized_string_set
    __swig_getmethods__["serialized_string"] = _freeswitch.Event_serialized_string_get
    if _newclass:serialized_string = _swig_property(_freeswitch.Event_serialized_string_get, _freeswitch.Event_serialized_string_set)
    __swig_setmethods__["mine"] = _freeswitch.Event_mine_set
    __swig_getmethods__["mine"] = _freeswitch.Event_mine_get
    if _newclass:mine = _swig_property(_freeswitch.Event_mine_get, _freeswitch.Event_mine_set)
    def __init__(self, *args): 
        this = _freeswitch.new_Event(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _freeswitch.delete_Event
    __del__ = lambda self : None;
    def chat_execute(self, *args): return _freeswitch.Event_chat_execute(self, *args)
    def chat_send(self, dest_proto=None): return _freeswitch.Event_chat_send(self, dest_proto)
    def serialize(self, format=None): return _freeswitch.Event_serialize(self, format)
    def setPriority(self, *args): return _freeswitch.Event_setPriority(self, *args)
    def getHeader(self, *args): return _freeswitch.Event_getHeader(self, *args)
    def getBody(self): return _freeswitch.Event_getBody(self)
    def getType(self): return _freeswitch.Event_getType(self)
    def addBody(self, *args): return _freeswitch.Event_addBody(self, *args)
    def addHeader(self, *args): return _freeswitch.Event_addHeader(self, *args)
    def delHeader(self, *args): return _freeswitch.Event_delHeader(self, *args)
    def fire(self): return _freeswitch.Event_fire(self)
Event_swigregister = _freeswitch.Event_swigregister
Event_swigregister(Event)

class EventConsumer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EventConsumer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EventConsumer, name)
    __repr__ = _swig_repr
    __swig_setmethods__["events"] = _freeswitch.EventConsumer_events_set
    __swig_getmethods__["events"] = _freeswitch.EventConsumer_events_get
    if _newclass:events = _swig_property(_freeswitch.EventConsumer_events_get, _freeswitch.EventConsumer_events_set)
    __swig_setmethods__["e_event_id"] = _freeswitch.EventConsumer_e_event_id_set
    __swig_getmethods__["e_event_id"] = _freeswitch.EventConsumer_e_event_id_get
    if _newclass:e_event_id = _swig_property(_freeswitch.EventConsumer_e_event_id_get, _freeswitch.EventConsumer_e_event_id_set)
    __swig_setmethods__["e_callback"] = _freeswitch.EventConsumer_e_callback_set
    __swig_getmethods__["e_callback"] = _freeswitch.EventConsumer_e_callback_get
    if _newclass:e_callback = _swig_property(_freeswitch.EventConsumer_e_callback_get, _freeswitch.EventConsumer_e_callback_set)
    __swig_setmethods__["e_subclass_name"] = _freeswitch.EventConsumer_e_subclass_name_set
    __swig_getmethods__["e_subclass_name"] = _freeswitch.EventConsumer_e_subclass_name_get
    if _newclass:e_subclass_name = _swig_property(_freeswitch.EventConsumer_e_subclass_name_get, _freeswitch.EventConsumer_e_subclass_name_set)
    __swig_setmethods__["e_cb_arg"] = _freeswitch.EventConsumer_e_cb_arg_set
    __swig_getmethods__["e_cb_arg"] = _freeswitch.EventConsumer_e_cb_arg_get
    if _newclass:e_cb_arg = _swig_property(_freeswitch.EventConsumer_e_cb_arg_get, _freeswitch.EventConsumer_e_cb_arg_set)
    __swig_setmethods__["enodes"] = _freeswitch.EventConsumer_enodes_set
    __swig_getmethods__["enodes"] = _freeswitch.EventConsumer_enodes_get
    if _newclass:enodes = _swig_property(_freeswitch.EventConsumer_enodes_get, _freeswitch.EventConsumer_enodes_set)
    __swig_setmethods__["node_index"] = _freeswitch.EventConsumer_node_index_set
    __swig_getmethods__["node_index"] = _freeswitch.EventConsumer_node_index_get
    if _newclass:node_index = _swig_property(_freeswitch.EventConsumer_node_index_get, _freeswitch.EventConsumer_node_index_set)
    def __init__(self, event_name=None, subclass_name="", len=5000): 
        this = _freeswitch.new_EventConsumer(event_name, subclass_name, len)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _freeswitch.delete_EventConsumer
    __del__ = lambda self : None;
    def bind(self, *args): return _freeswitch.EventConsumer_bind(self, *args)
    def pop(self, block=0, timeout=0): return _freeswitch.EventConsumer_pop(self, block, timeout)
    def cleanup(self): return _freeswitch.EventConsumer_cleanup(self)
EventConsumer_swigregister = _freeswitch.EventConsumer_swigregister
EventConsumer_swigregister(EventConsumer)

class CoreSession(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CoreSession, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CoreSession, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _freeswitch.delete_CoreSession
    __del__ = lambda self : None;
    __swig_setmethods__["session"] = _freeswitch.CoreSession_session_set
    __swig_getmethods__["session"] = _freeswitch.CoreSession_session_get
    if _newclass:session = _swig_property(_freeswitch.CoreSession_session_get, _freeswitch.CoreSession_session_set)
    __swig_setmethods__["channel"] = _freeswitch.CoreSession_channel_set
    __swig_getmethods__["channel"] = _freeswitch.CoreSession_channel_get
    if _newclass:channel = _swig_property(_freeswitch.CoreSession_channel_get, _freeswitch.CoreSession_channel_set)
    __swig_setmethods__["flags"] = _freeswitch.CoreSession_flags_set
    __swig_getmethods__["flags"] = _freeswitch.CoreSession_flags_get
    if _newclass:flags = _swig_property(_freeswitch.CoreSession_flags_get, _freeswitch.CoreSession_flags_set)
    __swig_setmethods__["allocated"] = _freeswitch.CoreSession_allocated_set
    __swig_getmethods__["allocated"] = _freeswitch.CoreSession_allocated_get
    if _newclass:allocated = _swig_property(_freeswitch.CoreSession_allocated_get, _freeswitch.CoreSession_allocated_set)
    __swig_setmethods__["cb_state"] = _freeswitch.CoreSession_cb_state_set
    __swig_getmethods__["cb_state"] = _freeswitch.CoreSession_cb_state_get
    if _newclass:cb_state = _swig_property(_freeswitch.CoreSession_cb_state_get, _freeswitch.CoreSession_cb_state_set)
    __swig_setmethods__["hook_state"] = _freeswitch.CoreSession_hook_state_set
    __swig_getmethods__["hook_state"] = _freeswitch.CoreSession_hook_state_get
    if _newclass:hook_state = _swig_property(_freeswitch.CoreSession_hook_state_get, _freeswitch.CoreSession_hook_state_set)
    __swig_setmethods__["cause"] = _freeswitch.CoreSession_cause_set
    __swig_getmethods__["cause"] = _freeswitch.CoreSession_cause_get
    if _newclass:cause = _swig_property(_freeswitch.CoreSession_cause_get, _freeswitch.CoreSession_cause_set)
    __swig_setmethods__["uuid"] = _freeswitch.CoreSession_uuid_set
    __swig_getmethods__["uuid"] = _freeswitch.CoreSession_uuid_get
    if _newclass:uuid = _swig_property(_freeswitch.CoreSession_uuid_get, _freeswitch.CoreSession_uuid_set)
    __swig_setmethods__["tts_name"] = _freeswitch.CoreSession_tts_name_set
    __swig_getmethods__["tts_name"] = _freeswitch.CoreSession_tts_name_get
    if _newclass:tts_name = _swig_property(_freeswitch.CoreSession_tts_name_get, _freeswitch.CoreSession_tts_name_set)
    __swig_setmethods__["voice_name"] = _freeswitch.CoreSession_voice_name_set
    __swig_getmethods__["voice_name"] = _freeswitch.CoreSession_voice_name_get
    if _newclass:voice_name = _swig_property(_freeswitch.CoreSession_voice_name_get, _freeswitch.CoreSession_voice_name_set)
    def insertFile(self, *args): return _freeswitch.CoreSession_insertFile(self, *args)
    def answer(self): return _freeswitch.CoreSession_answer(self)
    def preAnswer(self): return _freeswitch.CoreSession_preAnswer(self)
    def hangup(self, cause="normal_clearing"): return _freeswitch.CoreSession_hangup(self, cause)
    def hangupState(self): return _freeswitch.CoreSession_hangupState(self)
    def setVariable(self, *args): return _freeswitch.CoreSession_setVariable(self, *args)
    def setPrivate(self, *args): return _freeswitch.CoreSession_setPrivate(self, *args)
    def getPrivate(self, *args): return _freeswitch.CoreSession_getPrivate(self, *args)
    def getVariable(self, *args): return _freeswitch.CoreSession_getVariable(self, *args)
    def process_callback_result(self, *args): return _freeswitch.CoreSession_process_callback_result(self, *args)
    def say(self, *args): return _freeswitch.CoreSession_say(self, *args)
    def sayPhrase(self, *args): return _freeswitch.CoreSession_sayPhrase(self, *args)
    def hangupCause(self): return _freeswitch.CoreSession_hangupCause(self)
    def getState(self): return _freeswitch.CoreSession_getState(self)
    def recordFile(self, *args): return _freeswitch.CoreSession_recordFile(self, *args)
    def originate(self, *args): return _freeswitch.CoreSession_originate(self, *args)
    def destroy(self): return _freeswitch.CoreSession_destroy(self)
    def setDTMFCallback(self, *args): return _freeswitch.CoreSession_setDTMFCallback(self, *args)
    def speak(self, *args): return _freeswitch.CoreSession_speak(self, *args)
    def set_tts_parms(self, *args): return _freeswitch.CoreSession_set_tts_parms(self, *args)
    def set_tts_params(self, *args): return _freeswitch.CoreSession_set_tts_params(self, *args)
    def collectDigits(self, *args): return _freeswitch.CoreSession_collectDigits(self, *args)
    def getDigits(self, *args): return _freeswitch.CoreSession_getDigits(self, *args)
    def transfer(self, *args): return _freeswitch.CoreSession_transfer(self, *args)
    def read(self, *args): return _freeswitch.CoreSession_read(self, *args)
    def playAndGetDigits(self, *args): return _freeswitch.CoreSession_playAndGetDigits(self, *args)
    def streamFile(self, *args): return _freeswitch.CoreSession_streamFile(self, *args)
    def sleep(self, *args): return _freeswitch.CoreSession_sleep(self, *args)
    def flushEvents(self): return _freeswitch.CoreSession_flushEvents(self)
    def flushDigits(self): return _freeswitch.CoreSession_flushDigits(self)
    def setAutoHangup(self, *args): return _freeswitch.CoreSession_setAutoHangup(self, *args)
    def setHangupHook(self, *args): return _freeswitch.CoreSession_setHangupHook(self, *args)
    def ready(self): return _freeswitch.CoreSession_ready(self)
    def bridged(self): return _freeswitch.CoreSession_bridged(self)
    def answered(self): return _freeswitch.CoreSession_answered(self)
    def mediaReady(self): return _freeswitch.CoreSession_mediaReady(self)
    def waitForAnswer(self, *args): return _freeswitch.CoreSession_waitForAnswer(self, *args)
    def execute(self, *args): return _freeswitch.CoreSession_execute(self, *args)
    def sendEvent(self, *args): return _freeswitch.CoreSession_sendEvent(self, *args)
    def setEventData(self, *args): return _freeswitch.CoreSession_setEventData(self, *args)
    def getXMLCDR(self): return _freeswitch.CoreSession_getXMLCDR(self)
    def begin_allow_threads(self): return _freeswitch.CoreSession_begin_allow_threads(self)
    def end_allow_threads(self): return _freeswitch.CoreSession_end_allow_threads(self)
    def get_uuid(self): return _freeswitch.CoreSession_get_uuid(self)
    def get_cb_args(self): return _freeswitch.CoreSession_get_cb_args(self)
    def check_hangup_hook(self): return _freeswitch.CoreSession_check_hangup_hook(self)
    def run_dtmf_callback(self, *args): return _freeswitch.CoreSession_run_dtmf_callback(self, *args)
    def consoleLog(self, *args): return _freeswitch.CoreSession_consoleLog(self, *args)
    def consoleLog2(self, *args): return _freeswitch.CoreSession_consoleLog2(self, *args)
CoreSession_swigregister = _freeswitch.CoreSession_swigregister
CoreSession_swigregister(CoreSession)


def console_log(*args):
  return _freeswitch.console_log(*args)
console_log = _freeswitch.console_log

def console_log2(*args):
  return _freeswitch.console_log2(*args)
console_log2 = _freeswitch.console_log2

def console_clean_log(*args):
  return _freeswitch.console_clean_log(*args)
console_clean_log = _freeswitch.console_clean_log

def msleep(*args):
  return _freeswitch.msleep(*args)
msleep = _freeswitch.msleep

def bridge(*args):
  return _freeswitch.bridge(*args)
bridge = _freeswitch.bridge

def hanguphook(*args):
  return _freeswitch.hanguphook(*args)
hanguphook = _freeswitch.hanguphook

def dtmf_callback(*args):
  return _freeswitch.dtmf_callback(*args)
dtmf_callback = _freeswitch.dtmf_callback
class Session(CoreSession):
    __swig_setmethods__ = {}
    for _s in [CoreSession]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Session, name, value)
    __swig_getmethods__ = {}
    for _s in [CoreSession]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Session, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _freeswitch.new_Session(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _freeswitch.delete_Session
    __del__ = lambda self : None;
    def begin_allow_threads(self): return _freeswitch.Session_begin_allow_threads(self)
    def end_allow_threads(self): return _freeswitch.Session_end_allow_threads(self)
    def check_hangup_hook(self): return _freeswitch.Session_check_hangup_hook(self)
    def destroy(self): return _freeswitch.Session_destroy(self)
    def run_dtmf_callback(self, *args): return _freeswitch.Session_run_dtmf_callback(self, *args)
    def setInputCallback(self, *args): return _freeswitch.Session_setInputCallback(self, *args)
    def unsetInputCallback(self): return _freeswitch.Session_unsetInputCallback(self)
    def setHangupHook(self, *args): return _freeswitch.Session_setHangupHook(self, *args)
    def ready(self): return _freeswitch.Session_ready(self)
    __swig_setmethods__["cb_function"] = _freeswitch.Session_cb_function_set
    __swig_getmethods__["cb_function"] = _freeswitch.Session_cb_function_get
    if _newclass:cb_function = _swig_property(_freeswitch.Session_cb_function_get, _freeswitch.Session_cb_function_set)
    __swig_setmethods__["cb_arg"] = _freeswitch.Session_cb_arg_set
    __swig_getmethods__["cb_arg"] = _freeswitch.Session_cb_arg_get
    if _newclass:cb_arg = _swig_property(_freeswitch.Session_cb_arg_get, _freeswitch.Session_cb_arg_set)
    __swig_setmethods__["hangup_func"] = _freeswitch.Session_hangup_func_set
    __swig_getmethods__["hangup_func"] = _freeswitch.Session_hangup_func_get
    if _newclass:hangup_func = _swig_property(_freeswitch.Session_hangup_func_get, _freeswitch.Session_hangup_func_set)
    __swig_setmethods__["hangup_func_arg"] = _freeswitch.Session_hangup_func_arg_set
    __swig_getmethods__["hangup_func_arg"] = _freeswitch.Session_hangup_func_arg_get
    if _newclass:hangup_func_arg = _swig_property(_freeswitch.Session_hangup_func_arg_get, _freeswitch.Session_hangup_func_arg_set)
    def setPython(self, *args): return _freeswitch.Session_setPython(self, *args)
    def setSelf(self, *args): return _freeswitch.Session_setSelf(self, *args)
Session_swigregister = _freeswitch.Session_swigregister
Session_swigregister(Session)

# This file is compatible with both classic and new-style classes.

