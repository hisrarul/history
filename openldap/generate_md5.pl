#! /usr/bin/perl
#
# This small script generates an MD5 hash of 'secret' for use
# as a userPassword or rootpw value.
#
use Digest::MD5;
use MIME::Base64;
$ctx = Digest::MD5->new;
$ctx->add('Enter_your_password');
$hashedPasswd = '{MD5}' . encode_base64($ctx->digest,'');
print 'userPassword: ' .  $hashedPasswd . "\n";
