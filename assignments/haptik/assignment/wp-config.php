<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'database_name_here' );

/** MySQL database username */
define( 'DB_USER', 'username_here' );

/** MySQL database password */
define( 'DB_PASSWORD', 'password_here' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'beCT#_]??nzC|dtiJbj!pM=:b#i8#A+3IG2I20|5c[!fvfzB?9e*9IRfg$pM0`S)' );
define( 'SECURE_AUTH_KEY',  'Uh%@{9VlR|g|R}cQKhU{Tx20?uj}Lsma61W6?AKQ1aNX%muFaG+=tFS[u^|dX%gV' );
define( 'LOGGED_IN_KEY',    'T/pgWl.GW}nWb.UH/,hFo;=.>&4<nB:(Ij[C+y]b!P@+IrLTe/Mf@zQ}ajEZOpf9' );
define( 'NONCE_KEY',        'W^p(5.p.k,(&!HI+w8;agAP)[Pmej:KO:%`|}}=3N9Vc(Q,`a!6xQl**bXG:U(*w' );
define( 'AUTH_SALT',        'J.*7vAFQ3zDMPEOtazlsE(sfb(Jrj1Ip#|L^,Z@vwTXMlynUe)kR^ZT}fctBY8~e' );
define( 'SECURE_AUTH_SALT', 'ObID(717SN@WYZ56&@jWI1Vw><;6W&LcR7z_!uaT6HM7i&)BNb:[i3/dw?iXrPb+' );
define( 'LOGGED_IN_SALT',   'OPVVvftwDmT<8R{R1qR(oXd7t,TrcaxP:m1JO- @~~*!Ha3pJhwp^Hl^M1g$Epc;' );
define( 'NONCE_SALT',       '6l*oCb8ILVA!nX3{rRIAO8,n4r[xJNO,_:A@$;RB ^=B<T1%pbE}#K)vLdF~(#EG' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );
}

/** Sets up WordPress vars and included files. */
require_once( ABSPATH . 'wp-settings.php' );

