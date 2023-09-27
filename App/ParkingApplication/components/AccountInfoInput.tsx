import React, { useState } from 'react';
import { Button, StyleSheet } from 'react-native';

import Colors from '../constants/Colors';
import { ExternalLink } from './ExternalLink';
import { MonoText } from './StyledText';
import { View} from './Themed';
import { Text, TextInput } from 'react-native';


export default function AccountInfoInput({ path }: { path: string }) {
  const [accountId, setAccountId] = useState('');
  const [plateId, setPlateId] = useState('');
  return (
    <View>
      <View style={styles.getStartedContainer}>
        <Text> Account ID </Text>
        <TextInput style={styles.inputBox}
         onChangeText={accountId => setAccountId(accountId)}
        />
      </View>
      <View style={styles.getStartedContainer}>
        <Text> Liscence Plates </Text>
        <TextInput style={styles.inputBox}
          onChangeText={plateId => setPlateId(plateId)}
        />
      </View>
      <Button
        onPress={submitAccountInfo}
        title="Submit"
      />
    </View>
  );
}

function submitAccountInfo() {

}

const styles = StyleSheet.create({
  inputBox: {
    borderColor: '#5A5A5A',
    borderWidth: 1,
    width: 100,
    borderRadius: 5,
    textAlign: 'center'
  },
  getStartedContainer: {
    alignItems: 'center',
    marginHorizontal: 50,
    paddingBottom: 20
  },
  homeScreenFilename: {
    marginVertical: 7,
  },
  codeHighlightContainer: {
    borderRadius: 3,
    paddingHorizontal: 4,
  },
  getStartedText: {
    fontSize: 17,
    lineHeight: 24,
    textAlign: 'center',
  },
  helpContainer: {
    marginTop: 15,
    marginHorizontal: 20,
    alignItems: 'center',
  },
  helpLink: {
    paddingVertical: 15,
  },
  helpLinkText: {
    textAlign: 'center',
  },
});
