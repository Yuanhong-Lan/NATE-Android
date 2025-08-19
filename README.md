# NATE (Network Aware Testing Enhancer)
### Overview
#### 1.1 Network Related Faults (NRFs)
Network Related Faults (NRFs) refer to unexpected app behaviors under abnormal network conditions (only faults explicitly confirmed by the developers are called bugs in our context).

#### 1.2 Background
Nowadays, Android apps are becoming much more network-dependent, with increasingly network-related faults being observed, severely undermining user experience. Given that such faults are scattered in modern apps and require complex network patterns to trigger, their detection is challenging.

#### 1.3 Empirical Study
To date, we still lack a general and in-depth understanding of such faults. To fill this gap, we conduct the first empirical study on 154 real-world network-related bugs filtered from 42 diverse representative Android apps to investigate their characteristics, influences, triggering patterns, and origins.

#### 1.4 NATE
While existing Android testing approaches struggle with detecting such faults due to a lack of effective network events and efficient injection, we propose NATE on the basis of our study, a network-aware testing enhancer to empower existing general Android testing approaches to detect network-related faults. Based on curiosity-driven reinforcement learning, NATE conducts network-aware guidance to inject effective network events, enabling testing approaches to explore network-related extra app functionalities and detect network-related faults.



<br/>



### Publication
Please refer to our ASE 2025 paper "NATE: A Network-Aware Testing Enhancer for Network-Related Fault Detection in Android Apps" for more details. The paper will be published soon.



<br/>



### Empirical Study
#### 2.1 The Identified Real-World Network-Related Bugs
<details>

<summary>Here is the full list of the 154 identified real-world network-related bugs in our empirical study.</summary>

| APP | URL |
| --- | --- |
| AmazeFileManager | [https://github.com/TeamAmaze/AmazeFileManager/issues/1920](https://github.com/TeamAmaze/AmazeFileManager/issues/1920) |
| AnkiDroid | [https://github.com/ankidroid/Anki-Android/issues/17551](https://github.com/ankidroid/Anki-Android/issues/17551) |
| AnkiDroid | [https://github.com/ankidroid/Anki-Android/issues/13867](https://github.com/ankidroid/Anki-Android/issues/13867) |
| AnkiDroid | [https://github.com/ankidroid/Anki-Android/issues/13865](https://github.com/ankidroid/Anki-Android/issues/13865) |
| AnkiDroid | [https://github.com/ankidroid/Anki-Android/issues/12899](https://github.com/ankidroid/Anki-Android/issues/12899) |
| AnkiDroid | [https://github.com/ankidroid/Anki-Android/issues/12850](https://github.com/ankidroid/Anki-Android/issues/12850) |
| AnkiDroid | [https://github.com/ankidroid/Anki-Android/issues/12711](https://github.com/ankidroid/Anki-Android/issues/12711) |
| AnkiDroid | [https://github.com/ankidroid/Anki-Android/issues/9961](https://github.com/ankidroid/Anki-Android/issues/9961) |
| AnkiDroid | [https://github.com/ankidroid/Anki-Android/issues/17639](https://github.com/ankidroid/Anki-Android/issues/17639) |
| AnkiDroid | [https://github.com/ankidroid/Anki-Android/issues/12258](https://github.com/ankidroid/Anki-Android/issues/12258) |
| AnkiDroid | [https://github.com/ankidroid/Anki-Android/issues/10000](https://github.com/ankidroid/Anki-Android/issues/10000) |
| AnkiDroid | [https://github.com/ankidroid/Anki-Android/issues/6829](https://github.com/ankidroid/Anki-Android/issues/6829) |
| AntennaPod | [https://github.com/AntennaPod/AntennaPod/issues/7136](https://github.com/AntennaPod/AntennaPod/issues/7136) |
| AntennaPod | [https://github.com/AntennaPod/AntennaPod/issues/956](https://github.com/AntennaPod/AntennaPod/issues/956) |
| AntennaPod | [https://github.com/AntennaPod/AntennaPod/issues/2220](https://github.com/AntennaPod/AntennaPod/issues/2220) |
| AntennaPod | [https://github.com/AntennaPod/AntennaPod/issues/1942](https://github.com/AntennaPod/AntennaPod/issues/1942) |
| AntennaPod | [https://github.com/AntennaPod/AntennaPod/issues/2906](https://github.com/AntennaPod/AntennaPod/issues/2906) |
| AntennaPod | [https://github.com/AntennaPod/AntennaPod/issues/3196](https://github.com/AntennaPod/AntennaPod/issues/3196) |
| AntennaPod | [https://github.com/AntennaPod/AntennaPod/issues/2953](https://github.com/AntennaPod/AntennaPod/issues/2953) |
| AntennaPod | [https://github.com/AntennaPod/AntennaPod/issues/5255](https://github.com/AntennaPod/AntennaPod/issues/5255) |
| AntennaPod | [https://github.com/AntennaPod/AntennaPod/issues/4227](https://github.com/AntennaPod/AntennaPod/issues/4227) |
| AntennaPod | [https://github.com/AntennaPod/AntennaPod/issues/5936](https://github.com/AntennaPod/AntennaPod/issues/5936) |
| ConnectBot | [https://github.com/connectbot/connectbot/issues/439](https://github.com/connectbot/connectbot/issues/439) |
| DuckDuckGo | [https://github.com/duckduckgo/Android/issues/3801](https://github.com/duckduckgo/Android/issues/3801) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1875240](https://bugzilla.mozilla.org/show_bug.cgi?id=1875240) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1891257](https://bugzilla.mozilla.org/show_bug.cgi?id=1891257) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1914416](https://bugzilla.mozilla.org/show_bug.cgi?id=1914416) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1909562](https://bugzilla.mozilla.org/show_bug.cgi?id=1909562) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1926859](https://bugzilla.mozilla.org/show_bug.cgi?id=1926859) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1926853](https://bugzilla.mozilla.org/show_bug.cgi?id=1926853) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1946571](https://bugzilla.mozilla.org/show_bug.cgi?id=1946571) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1945035](https://bugzilla.mozilla.org/show_bug.cgi?id=1945035) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1918628](https://bugzilla.mozilla.org/show_bug.cgi?id=1918628) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1906466](https://bugzilla.mozilla.org/show_bug.cgi?id=1906466) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1906323](https://bugzilla.mozilla.org/show_bug.cgi?id=1906323) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1876061](https://bugzilla.mozilla.org/show_bug.cgi?id=1876061) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1813835](https://bugzilla.mozilla.org/show_bug.cgi?id=1813835) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1810842](https://bugzilla.mozilla.org/show_bug.cgi?id=1810842) |
| Firefox | [https://github.com/mozilla-mobile/fenix/issues/18040](https://github.com/mozilla-mobile/fenix/issues/18040) |
| Firefox | [https://github.com/mozilla-mobile/fenix/issues/17086](https://github.com/mozilla-mobile/fenix/issues/17086) |
| Firefox | [https://github.com/mozilla-mobile/fenix/issues/9461](https://github.com/mozilla-mobile/fenix/issues/9461) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1933077](https://bugzilla.mozilla.org/show_bug.cgi?id=1933077) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1809311](https://bugzilla.mozilla.org/show_bug.cgi?id=1809311) |
| Firefox | [https://github.com/mozilla-mobile/fenix/issues/18481](https://github.com/mozilla-mobile/fenix/issues/18481) |
| Firefox | [https://github.com/mozilla-mobile/fenix/issues/17762](https://github.com/mozilla-mobile/fenix/issues/17762) |
| Firefox | [https://github.com/mozilla-mobile/fenix/issues/769](https://github.com/mozilla-mobile/fenix/issues/769) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1940448](https://bugzilla.mozilla.org/show_bug.cgi?id=1940448) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1934486](https://bugzilla.mozilla.org/show_bug.cgi?id=1934486) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1933037](https://bugzilla.mozilla.org/show_bug.cgi?id=1933037) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1868469](https://bugzilla.mozilla.org/show_bug.cgi?id=1868469) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1867815](https://bugzilla.mozilla.org/show_bug.cgi?id=1867815) |
| Firefox | [https://bugzilla.mozilla.org/show_bug.cgi?id=1792950](https://bugzilla.mozilla.org/show_bug.cgi?id=1792950) |
| K9Mail | [https://github.com/thunderbird/thunderbird-android/issues/8242](https://github.com/thunderbird/thunderbird-android/issues/8242) |
| K9Mail | [https://github.com/thunderbird/thunderbird-android/issues/7870](https://github.com/thunderbird/thunderbird-android/issues/7870) |
| K9Mail | [https://github.com/thunderbird/thunderbird-android/issues/5425](https://github.com/thunderbird/thunderbird-android/issues/5425) |
| K9Mail | [https://github.com/thunderbird/thunderbird-android/issues/5366](https://github.com/thunderbird/thunderbird-android/issues/5366) |
| K9Mail | [https://github.com/thunderbird/thunderbird-android/issues/4708](https://github.com/thunderbird/thunderbird-android/issues/4708) |
| Materialistic | [https://github.com/hidroh/materialistic/issues/775](https://github.com/hidroh/materialistic/issues/775) |
| Materialistic | [https://github.com/hidroh/materialistic/issues/293](https://github.com/hidroh/materialistic/issues/293) |
| Materialistic | [https://github.com/hidroh/materialistic/issues/453](https://github.com/hidroh/materialistic/issues/453) |
| Materialistic | [https://github.com/hidroh/materialistic/issues/448](https://github.com/hidroh/materialistic/issues/448) |
| Materialistic | [https://github.com/hidroh/materialistic/issues/309](https://github.com/hidroh/materialistic/issues/309) |
| Materialistic | [https://github.com/hidroh/materialistic/issues/765](https://github.com/hidroh/materialistic/issues/765) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/11573](https://github.com/TeamNewPipe/NewPipe/issues/11573) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/3923](https://github.com/TeamNewPipe/NewPipe/issues/3923) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/4920](https://github.com/TeamNewPipe/NewPipe/issues/4920) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/4432](https://github.com/TeamNewPipe/NewPipe/issues/4432) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/5452](https://github.com/TeamNewPipe/NewPipe/issues/5452) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/5263](https://github.com/TeamNewPipe/NewPipe/issues/5263) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/8898](https://github.com/TeamNewPipe/NewPipe/issues/8898) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/6298](https://github.com/TeamNewPipe/NewPipe/issues/6298) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/11029](https://github.com/TeamNewPipe/NewPipe/issues/11029) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/9358](https://github.com/TeamNewPipe/NewPipe/issues/9358) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/11191](https://github.com/TeamNewPipe/NewPipe/issues/11191) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/1527](https://github.com/TeamNewPipe/NewPipe/issues/1527) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/938](https://github.com/TeamNewPipe/NewPipe/issues/938) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/2268](https://github.com/TeamNewPipe/NewPipe/issues/2268) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/2171](https://github.com/TeamNewPipe/NewPipe/issues/2171) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/2421](https://github.com/TeamNewPipe/NewPipe/issues/2421) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/2418](https://github.com/TeamNewPipe/NewPipe/issues/2418) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/3725](https://github.com/TeamNewPipe/NewPipe/issues/3725) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/3368](https://github.com/TeamNewPipe/NewPipe/issues/3368) |
| NewPipe | [https://github.com/TeamNewPipe/NewPipe/issues/2765](https://github.com/TeamNewPipe/NewPipe/issues/2765) |
| RunnerUp | [https://github.com/jonasoreland/runnerup/issues/931](https://github.com/jonasoreland/runnerup/issues/931) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/11898](https://github.com/signalapp/Signal-Android/issues/11898) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/11202](https://github.com/signalapp/Signal-Android/issues/11202) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/9814](https://github.com/signalapp/Signal-Android/issues/9814) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/7819](https://github.com/signalapp/Signal-Android/issues/7819) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/7733](https://github.com/signalapp/Signal-Android/issues/7733) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/7638](https://github.com/signalapp/Signal-Android/issues/7638) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/6644](https://github.com/signalapp/Signal-Android/issues/6644) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/6447](https://github.com/signalapp/Signal-Android/issues/6447) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/6003](https://github.com/signalapp/Signal-Android/issues/6003) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/5353](https://github.com/signalapp/Signal-Android/issues/5353) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/2639](https://github.com/signalapp/Signal-Android/issues/2639) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/1264](https://github.com/signalapp/Signal-Android/issues/1264) |
| Signal | [https://github.com/signalapp/Signal-Android/issues/7647](https://github.com/signalapp/Signal-Android/issues/7647) |
| SuntimesWidget | [https://github.com/forrestguice/SuntimesWidget/issues/420](https://github.com/forrestguice/SuntimesWidget/issues/420) |
| Wikipedia | [https://github.com/wikimedia/apps-android-wikipedia/pull/4102](https://github.com/wikimedia/apps-android-wikipedia/pull/4102) |
| Wikipedia | [https://github.com/wikimedia/apps-android-wikipedia/pull/4650](https://github.com/wikimedia/apps-android-wikipedia/pull/4650) |
| Wikipedia | [https://github.com/wikimedia/apps-android-wikipedia/pull/4606](https://github.com/wikimedia/apps-android-wikipedia/pull/4606) |
| Wikipedia | [https://github.com/wikimedia/apps-android-wikipedia/pull/5221](https://github.com/wikimedia/apps-android-wikipedia/pull/5221) |
| Wikipedia | [https://github.com/wikimedia/apps-android-wikipedia/pull/3781](https://github.com/wikimedia/apps-android-wikipedia/pull/3781) |
| Wikipedia | [https://github.com/wikimedia/apps-android-wikipedia/pull/2962](https://github.com/wikimedia/apps-android-wikipedia/pull/2962) |
| Wikipedia | [https://github.com/wikimedia/apps-android-wikipedia/pull/1991](https://github.com/wikimedia/apps-android-wikipedia/pull/1991) |
| Wikipedia | [https://github.com/wikimedia/apps-android-wikipedia/pull/545](https://github.com/wikimedia/apps-android-wikipedia/pull/545) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/21283](https://github.com/wordpress-mobile/WordPress-Android/issues/21283) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/21087](https://github.com/wordpress-mobile/WordPress-Android/issues/21087) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/20905](https://github.com/wordpress-mobile/WordPress-Android/issues/20905) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/20531](https://github.com/wordpress-mobile/WordPress-Android/issues/20531) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/19578](https://github.com/wordpress-mobile/WordPress-Android/issues/19578) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/19533](https://github.com/wordpress-mobile/WordPress-Android/issues/19533) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/19388](https://github.com/wordpress-mobile/WordPress-Android/issues/19388) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/18878](https://github.com/wordpress-mobile/WordPress-Android/issues/18878) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/17463](https://github.com/wordpress-mobile/WordPress-Android/issues/17463) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/17154](https://github.com/wordpress-mobile/WordPress-Android/issues/17154) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/16997](https://github.com/wordpress-mobile/WordPress-Android/issues/16997) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/16760](https://github.com/wordpress-mobile/WordPress-Android/issues/16760) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/15590](https://github.com/wordpress-mobile/WordPress-Android/issues/15590) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/14840](https://github.com/wordpress-mobile/WordPress-Android/issues/14840) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/13197](https://github.com/wordpress-mobile/WordPress-Android/issues/13197) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/11357](https://github.com/wordpress-mobile/WordPress-Android/issues/11357) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/10836](https://github.com/wordpress-mobile/WordPress-Android/issues/10836) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/10546](https://github.com/wordpress-mobile/WordPress-Android/issues/10546) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/10545](https://github.com/wordpress-mobile/WordPress-Android/issues/10545) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/10200](https://github.com/wordpress-mobile/WordPress-Android/issues/10200) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/10154](https://github.com/wordpress-mobile/WordPress-Android/issues/10154) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/10021](https://github.com/wordpress-mobile/WordPress-Android/issues/10021) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9985](https://github.com/wordpress-mobile/WordPress-Android/issues/9985) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9949](https://github.com/wordpress-mobile/WordPress-Android/issues/9949) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9935](https://github.com/wordpress-mobile/WordPress-Android/issues/9935) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9933](https://github.com/wordpress-mobile/WordPress-Android/issues/9933) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9843](https://github.com/wordpress-mobile/WordPress-Android/issues/9843) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9804](https://github.com/wordpress-mobile/WordPress-Android/issues/9804) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9790](https://github.com/wordpress-mobile/WordPress-Android/issues/9790) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9760](https://github.com/wordpress-mobile/WordPress-Android/issues/9760) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9567](https://github.com/wordpress-mobile/WordPress-Android/issues/9567) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9563](https://github.com/wordpress-mobile/WordPress-Android/issues/9563) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9562](https://github.com/wordpress-mobile/WordPress-Android/issues/9562) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9560](https://github.com/wordpress-mobile/WordPress-Android/issues/9560) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/9556](https://github.com/wordpress-mobile/WordPress-Android/issues/9556) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/8402](https://github.com/wordpress-mobile/WordPress-Android/issues/8402) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/4332](https://github.com/wordpress-mobile/WordPress-Android/issues/4332) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/3683](https://github.com/wordpress-mobile/WordPress-Android/issues/3683) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/2325](https://github.com/wordpress-mobile/WordPress-Android/issues/2325) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/2270](https://github.com/wordpress-mobile/WordPress-Android/issues/2270) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/1936](https://github.com/wordpress-mobile/WordPress-Android/issues/1936) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/1568](https://github.com/wordpress-mobile/WordPress-Android/issues/1568) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/1453](https://github.com/wordpress-mobile/WordPress-Android/issues/1453) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/1130](https://github.com/wordpress-mobile/WordPress-Android/issues/1130) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/1098](https://github.com/wordpress-mobile/WordPress-Android/issues/1098) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/1049](https://github.com/wordpress-mobile/WordPress-Android/issues/1049) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/736](https://github.com/wordpress-mobile/WordPress-Android/issues/736) |
| WordPress | [https://github.com/wordpress-mobile/WordPress-Android/issues/688](https://github.com/wordpress-mobile/WordPress-Android/issues/688) |


</details>



<br/>



### NATE Tool
#### 3.1 Introduction
NATE is a network-aware testing enhancer guided by RL-based curiosity-driven exploration, to empower existing general Android testing approaches to detect network-related faults.



#### 3.2 Requirements
+ Python: Tested on Python 3.11
+ Android: The normal functioning of ADB commands in the command line.



#### 3.3 Integration
Integrating NATE with a general Android testing approach is very straightforward and could be achieved both intrusively and non-intrusively.

##### 3.3.1 Intrusively
To directly integrate NATE with a general Android testing approach:

1. Create a Python project. (If the approach itself is Python-based, skip this step.)
2. Put `NATE` and `android_testing_utils` under the root directory of your Python project to avoid import issues. (If you put it elsewhere, you need to adjust the imports yourself.)
3. For each testing step of the general testing approach, call NATE and pass the required <u>App State</u> and <u>Selected App Event</u>.

##### 3.3.2 Non-Intrusively
Very similar to the workflow in 3.3.1. The only difference is that the required <u>App State</u> and <u>Selected App Event</u> by NATE is obtained non-intrusively, rather than passed by direct function calls. For example, by capturing the real-time log stream from the general testing tools, the required step-wise <u>App State</u> and <u>Selected App Event</u> could be extracted in time.



#### 3.4 Usage
Before the test starts, initialize a `NATE_MAIN` instance from `NATE/nate_main.py`:

+ **device_id**: The device ID of the target device (e.g., "emulator-5554")
+ **package_name**: The package name of the App Under Test (e.g., org.mozilla.fenix.debug)
+ **use_pure_random**: To randomly inject network events without guidance, enable this option
+ **auto_action:** Whether the number of actions in each state is known when testing; if not, enable this option
+ **netflow_strategy**: As the network-related APIs in different Android Versions are different, we need different strategies. Currently, we have implemented:
    - `NetFlowStrategy.mAppUidStatsMap` Tested on Android 14 Emulators
    - `NetFlowStrategy.xt_qtaguid` Tested on Android 9 Emulators

_**<u>NOTING!!!  Before starting NATE, it is suggested to try the network monitoring adb commands on your target Android Version in advance. You may need to implement yours for your Android Version.</u>**_

At each test loop step t+1, call `NATE_MAIN.nate_step`:

+ **raw_app_state**: The state identifier on step t
+ **selected_action**: The app event on step t, if using auto_action, this is the action identifier; if not, this is the action index
+ **target_app_state**: The state identifier on step t+1, this may be None when an end state is met
+ **target_selected_action**: The app event on step t+1, if using auto_action, this is the action identifier; if not, this is the action index
+ **raw_action_count**: If not auto_action, provide the number of actions on step t, else None
+ **target_action_count**: If not auto_action, provide the number of actions on step t+1, else None

NATE will automatically learn and inject network events when appropriate.



#### 3.5 Outputs
Call `NATE_MAIN.persist_history` to persist data.

+ **NATE/guidance/q_table**: The learned Q-Table.
+ **NATE/network_injector/injection_record**: The injection history.
+ **NATE/network_monitor/network_monitor_record**: Network monitoring details.



