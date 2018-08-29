function varargout = view_image_gui(varargin)
% VIEW_IMAGE_GUI MATLAB code for view_image_gui.fig
%      VIEW_IMAGE_GUI, by itself, creates a new VIEW_IMAGE_GUI or raises the existing
%      singleton*.
%
%      H = VIEW_IMAGE_GUI returns the handle to a new VIEW_IMAGE_GUI or the handle to
%      the existing singleton*.
%
%      VIEW_IMAGE_GUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in VIEW_IMAGE_GUI.M with the given input arguments.
%
%      VIEW_IMAGE_GUI('Property','Value',...) creates a new VIEW_IMAGE_GUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before view_image_gui_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to view_image_gui_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help view_image_gui

% Last Modified by GUIDE v2.5 29-Aug-2018 13:15:20

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @view_image_gui_OpeningFcn, ...
                   'gui_OutputFcn',  @view_image_gui_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before view_image_gui is made visible.
function view_image_gui_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to view_image_gui (see VARARGIN)

% Choose default command line output for view_image_gui
handles.output = hObject;

load_params;
handles.hf = figure;
handles.rootdir = rootdir;

% Update handles structure
guidata(hObject, handles);

load_image(hObject, handles, 1, 1);

% UIWAIT makes view_image_gui wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = view_image_gui_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function worm_input_Callback(hObject, eventdata, handles)
% hObject    handle to worm_input (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of worm_input as text
%        str2double(get(hObject,'String')) returns contents of worm_input as a double


% --- Executes during object creation, after setting all properties.
function worm_input_CreateFcn(hObject, eventdata, handles)
% hObject    handle to worm_input (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function image_input_Callback(hObject, eventdata, handles)
% hObject    handle to image_input (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of image_input as text
%        str2double(get(hObject,'String')) returns contents of image_input as a double


% --- Executes during object creation, after setting all properties.
function image_input_CreateFcn(hObject, eventdata, handles)
% hObject    handle to image_input (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in go_button.
function go_button_Callback(hObject, eventdata, handles)
% hObject    handle to go_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
worm_id = str2double(handles.worm_input.String);
image_id = str2double(handles.worm_input.String);
load_image(hObject, handles, worm_id, image_id);

% --- Executes on button press in prev_button.
function prev_button_Callback(hObject, eventdata, handles)
% hObject    handle to prev_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
worm_id = str2double(handles.worm_input.String);
image_id = handles.image_id - 1;
load_image(hObject, handles, worm_id, image_id);


% --- Executes on button press in next_button.
function next_button_Callback(hObject, eventdata, handles)
% hObject    handle to next_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
worm_id = str2double(handles.worm_input.String);
image_id = handles.image_id + 1;
load_image(hObject, handles, worm_id, image_id);

function load_image(hObject, handles, worm_id, image_id)
imgpath = sprintf('%s/Worm%d/Image/Image_%d.tiff', handles.rootdir, worm_id, image_id);
im = imread(imgpath);
figure(handles.hf);
imshow(im);
handles.worm_id = worm_id;
handles.image_id = image_id;
handles.worm_inpug.String = num2str(worm_id);
handles.image_input.String = num2str(image_id);
guidata(hObject, handles);
