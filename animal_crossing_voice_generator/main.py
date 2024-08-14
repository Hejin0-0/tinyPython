from gtts import gTTS  # Google Text-to-Speech library // 텍스트를 음성으로 변환하는 Google Text-to-Speech 라이브러리
from pydub import AudioSegment  # Pydub library for audio manipulation // 오디오 조작을 위한 Pydub 라이브러리
from pydub.playback import play  # Pydub library function to play audio // 오디오 재생을 위한 Pydub 라이브러리 함수
import random  # Standard library for generating random numbers // 랜덤 숫자 생성을 위한 표준 라이브러리
import os  # Standard library for operating system functions // 운영 체제 기능을 위한 표준 라이브러리

# Create directories if they do not exist // 디렉토리가 없으면 생성
def create_directories():
    os.makedirs('samples', exist_ok=True)
    os.makedirs('result', exist_ok=True)

# Convert text to speech and save to file // 텍스트를 음성으로 변환하여 파일로 저장
def text_to_speech(letter):
    tts = gTTS(letter, lang='ko')
    file_path = f'samples/{letter}.mp3'
    tts.save(file_path)
    return file_path

# Load and modify the audio segment for the given letter // 주어진 문자의 오디오 세그먼트 로드 및 수정
def get_modified_audio_segment(letter):
    file_path = f'samples/{letter}.mp3'

    # Load existing audio file or generate new one // 기존 오디오 파일 로드 또는 새로 생성
    if not os.path.isfile(file_path):
        text_to_speech(letter)

    letter_sound = AudioSegment.from_mp3(file_path)
    raw = letter_sound.raw_data[5000:-5000]  # Extract raw audio data excluding the beginning and end portions // 시작과 끝 부분을 제외한 원시 오디오 데이터 추출

    # Generate a random octave factor // 랜덤 옥타브 계수 생성
    octaves = 2.0 + random.random() * 0.35
    frame_rate = int(letter_sound.frame_rate * (2.0 ** octaves))  # Adjust the frame rate based on octave factor // 옥타브 계수에 따라 프레임 레이트 조정

    # Create a new audio segment with adjusted frame rate // 조정된 프레임 레이트로 새로운 오디오 세그먼트 생성
    new_sound = letter_sound._spawn(raw, overrides={'frame_rate': frame_rate})
    new_sound = new_sound.set_frame_rate(44100)
    return new_sound

# Main function to process the entire text string // 전체 텍스트 문자열을 처리하는 메인 함수
def process_text_to_speech(string):
    create_directories()
    result_sound = None

    for letter in string:
        if letter == ' ':
            # Create a silent segment of audio for spaces // 공백에 대한 무음 오디오 세그먼트 생성
            new_sound = AudioSegment.silent(duration=1000)  # Duration in milliseconds // 밀리초 단위의 지속 시간
        else:
            new_sound = get_modified_audio_segment(letter)

        # Combine the new sound with the result_sound // 새 소리를 result_sound와 결합
        result_sound = new_sound if result_sound is None else result_sound + new_sound

    # Play the final combined sound // 최종 결합된 소리 재생
    play(result_sound)
    # Export the final combined sound to a file // 최종 결합된 소리를 파일로 내보내기
    result_sound.export(f'result/{string}.mp3', format='mp3')

# Example usage // 예제 사용법
if __name__ == "__main__":
    text = '안녕하세요 너굴 상회입니다'
    process_text_to_speech(text)


"""
  관련 문서:
  - gTTS Documentation : https://gtts.readthedocs.io/en/latest/ // gTTS 문서
  - pydub Documentation : https://pydub.com/ // pydub 문서
  + https://github.com/jiaaro/pydub.git
  - os.makedirs() : https://docs.python.org/3/library/os.html#os.makedirs // os.makedirs() 함수
  - AudioSegment Documentation :https://pydub.com/usage/#using-audiorecord // AudioSegment 문서
  - pydub.playback.play() : https://pydub.com/usage/#playing-audio // pydub.playback.play() 함수
"""