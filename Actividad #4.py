
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>392</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QDialogButtonBox" name="Guardar">
   <property name="geometry">
    <rect>
     <x>310</x>
     <y>330</y>
     <width>81</width>
     <height>241</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Vertical</enum>
   </property>
   <property name="standardButtons">
    <set>QDialogButtonBox::Cancel|QDialogButtonBox::Ok</set>
   </property>
  </widget>
  <widget class="QLabel" name="DestinoX">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>30</y>
     <width>141</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Destino X</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="lineEdit">
   <property name="geometry">
    <rect>
     <x>80</x>
     <y>40</y>
     <width>113</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>34</string>
   </property>
  </widget>
  <widget class="QLabel" name="DestinoY">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>80</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Destino Y</string>
   </property>
  </widget>
  <widget class="QLabel" name="Velocidad">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>130</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Velocidad</string>
   </property>
  </widget>
  <widget class="QLabel" name="Red">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>190</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Red</string>
   </property>
  </widget>
  <widget class="QLabel" name="Green">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>240</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Green</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_6">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>290</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Blue</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="lineEdit_2">
   <property name="geometry">
    <rect>
     <x>80</x>
     <y>80</y>
     <width>113</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>68</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="lineEdit_3">
   <property name="geometry">
    <rect>
     <x>80</x>
     <y>130</y>
     <width>113</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>124</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="lineEdit_4">
   <property name="geometry">
    <rect>
     <x>80</x>
     <y>180</y>
     <width>113</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>8</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="lineEdit_5">
   <property name="geometry">
    <rect>
     <x>80</x>
     <y>240</y>
     <width>113</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>2</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="lineEdit_6">
   <property name="geometry">
    <rect>
     <x>80</x>
     <y>290</y>
     <width>113</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>4</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>Guardar</sender>
   <signal>accepted()</signal>
   <receiver>Dialog</receiver>
   <slot>accept()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>248</x>
     <y>254</y>
    </hint>
    <hint type="destinationlabel">
     <x>157</x>
     <y>274</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>Guardar</sender>
   <signal>rejected()</signal>
   <receiver>Dialog</receiver>
   <slot>reject()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>316</x>
     <y>260</y>
    </hint>
    <hint type="destinationlabel">
     <x>286</x>
     <y>274</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>
